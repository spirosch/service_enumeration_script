import subprocess
import os


def read_input_file(filename):
    with open(filename, 'r') as file:
        hosts_and_ports = file.readlines()
    return [line.strip() for line in hosts_and_ports]


def run_rustscan(host, ports):
    ports_str = ','.join(ports)
    command = f"rustscan -a {host} -p {ports_str} -- -sV"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    return result.stdout


def parse_rustscan_output(output):
    services = []
    lines = output.split('\n')
    for line in lines:
        if 'open' in line:
            services.append(line.strip())
    return services


def write_output_file(output_filename, results):
    with open(output_filename, 'w') as file:
        for host, services in results.items():
            file.write(f"Host: {host}\n")
            for service in services:
                file.write(f"  {service}\n")
            file.write("\n")


def main():
    input_filename = 'hosts_and_ports_per_host.txt'
    output_filename = 'identified_services.txt'

    if not os.path.exists(input_filename):
        print(f"Input file {input_filename} does not exist.")
        return

    hosts_and_ports = read_input_file(input_filename)
    results = {}

    for entry in hosts_and_ports:
        parts = entry.split(':')
        host = parts[0]
        ports = parts[1].split(',')
        print(f"Scanning {host} on ports {ports}...")
        rustscan_output = run_rustscan(host, ports)
        services = parse_rustscan_output(rustscan_output)
        results[host] = services

    write_output_file(output_filename, results)
    print(f"Results written to {output_filename}")


if __name__ == "__main__":
    main()
