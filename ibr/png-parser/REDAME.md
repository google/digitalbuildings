## Instructions for Running the PNG Parser:

1. Compile the proto definition to python classes:
	- Install latest release of protocol buffers
	    - go to [https://developers.google.com/protocol-buffers/docs/downloads]()
	    - click on latest version release page
	    - click on protobuf-$VERSION-$PLATFORM.zip to download the protocol buffers pre-built binary
	    - unzip downloaded file
	    - place bin/protoc somewhere in your $PATH
	- move to current directory `cd digitalbuildings/ibr/png-parser`
	- compile the proto definition: `protoc -I=../ibr-sdk/proto/ --python_out=. ibr.proto`

2. Run the PNG Parser
    - `bazel build`
    - `bazel-bin/CreateIBR [PATH_TO_INPUT_BITMAP]`
    - You will see output IBR file is created in the current directory with the name new_ibr.ibr