# Video Object Detection Protobufs
This repo holds the protobuf files for the protobuf messages that are exchanged between the various services.

Once a frame is retrieved from a source, it is placed in a message then published to a reddis channel. Another service picks up the message and uses it for to request an inference after which it is placed on another channel with the prediction output.

Finally other services like the web service take the message from the channel and make it available to a react app via HTTP EventSource.

## Related Projects
- https://github.com/kunadawa/video-object-detection
- https://github.com/kunadawa/object-detection-event-web-server
- https://github.com/kunadawa/object-detection-react-app
