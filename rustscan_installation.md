1. **Download and Install RustScan for ARM64**: RustScan may not have pre-built binaries for ARM64. However, you can build it from the source. Follow these steps:

    a. **Install Rust**:
    ```sh
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    source $HOME/.cargo/env
    ```

    b. **Clone RustScan Repository**:
    ```sh
    git clone https://github.com/RustScan/RustScan.git
    cd RustScan
    ```

    c. **Build RustScan**:
    ```sh
    cargo build --release
    ```

    d. **Move the binary to a directory in your PATH**:
    ```sh
    sudo mv target/release/rustscan /usr/local/bin/
    ```

2. **Verify RustScan Installation**: Check that RustScan is installed and available:
    ```sh
    rustscan
    ```


