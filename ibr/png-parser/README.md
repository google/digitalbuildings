## Instructions for Running the PNG Parser:

1. Install Bazel
    - Check if you have Bazel installed already using command `bazel --version`.
    - If no version number is shown, follow instruction [here](https://docs.bazel.build/versions/master/install.html).

2. Compile the proto definition to python classes(Note: the compiled proto definition is already included in this repo. These instructures are only for your reference in case you would like to compiler your own proto definition.)
	- move to current directory `cd digitalbuildings/ibr/png-parser`
	- Install latest release of Protocol Compiler
	    - Go to [Download Protocol Compiler](https://developers.google.com/protocol-buffers/docs/downloads)
	    - Click on latest version release page
	    - According to your environment, click on the appropriate `protoc-$VERSION-$PLATFORM.zip` to download the protocol buffers pre-built binary
	    - Unzip downloaded file
	    - Place `bin/protoc` somewhere in your `$PATH`
	- Install latest release of Protobuf Python Runtime Library
	    - `pip3 install --upgrade protobuf`
	- compile the proto definition (default output python module name: ibr_pb2.py): `protoc -I=../ibr-sdk/proto/ --python_out=. ibr.proto`

3. Run the PNG Parser
    - Install protobuf Python runtime library `pip3 install --upgrade protobuf`
    - `bazel build //...`
    - `bazel-bin/create_ibr [PATH_TO_INPUT_BITMAP]`
    - You will see output IBR file is created in the current directory with the name $INPUT_FILE_NAME.ibr