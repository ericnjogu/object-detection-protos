# Object Detection Protobufs
This repo holds the protobuf files for the protobuf messages that are exchanged between the various services.

Once a frame is retrieved from a source, it is placed in a message then published to a reddis channel. Another service picks up the message and uses it for to request an inference after which it is placed on another channel with the prediction output.

Finally other services like the web service take the message from the channel and make it available to a react app via HTTP EventSource.

## Setup
- install Conda
- create conda environment

 `conda env create -f env.yaml`

- clone or download the [tensorflow serving repo](https://github.com/tensorflow/serving)
- Download or clone the [tensorflow core repo](https://github.com/tensorflow/tensorflow)
- generate the tensor flow prediction service python grpc stubs - note the tensorflow core and tensorflow serving repo local roots have been given to resolve the protobuf dependencies

 `python -m grpc_tools.protoc -I ~/tensorflow-serving-repo/ -I ~/tensorflow-core-repo --grpc_python_out=generated/ --python_out=generated ~/tensorflow-serving-repo/tensorflow_serving/apis/*.proto`

- generate the object detection protobuf message types, client, server grpc code.

 `python -m grpc_tools.protoc -I . --grpc_python_out=./generated/ --python_out=./generated detection_handler.proto`

## Related Projects
- https://github.com/kunadawa/video-object-detection
- https://github.com/kunadawa/object-detection-event-web-server
- https://github.com/kunadawa/object-detection-react-app
