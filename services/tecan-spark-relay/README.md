# `service.tecan-spark-relay`

The `service.tecan-spark-relay` is the service layer for interacting with a [Tecan Spark® Multimode Plate Reader](https://lifesciences.tecan.com/multimode-plate-reader) through the SparkControl API provided by Tecan. This API is not available publicly, so please contact your customer service representiative at Tecan to find out how you can access it.

## Minimum Requirements

- `.NET 5.0`

## Usage

- Install dependencies:

  ```
  dotnet restore
  ```

- Start auxiliary containers:

  ```
  make dependencies
  ```

- Export the following environment variables to the current shell:

  ```
  export MANAGER_DEVICE_NAME=<a unique name for the current device>
  export FORWARDER_DATA_GATEWAY_URL=<the base URL for the data-gateway service>
  ```

  Other environment variables that can be configured can be found in [`Config.cs`](Config.cs).

- Run the server:

  ```
  dotnet run server
  ```

## How it Works

Upon receiving a protocol trigger, the `service.tecan-spark-relay` generates a corresponding method XML file that can be understood by the Spark®, based on the protocol's name and spec. For an example of how this XML file looks like, see the [method XML file template for the MeasureAbsorbance protocol](Methods/MeasureAbsorbance/Method.xml).

This method XML file is then passed to the SparkControl API to be executed. While the method is being executed, the `service.tecan-spark-relay` is blocked from handling new protocol triggers. You can view the method while it's being executed through the SparkControl Dashboard. If the Spark® stops running midway through, the execution will not complete successfully.

Once the method has completed execution, an XML file containing the measurement data produced by the Spark® is exported via the API. See [here for an example](Methods/MeasureAbsorbance/Export.xml) of this data export XML file. This file is then parsed and transformed into a format that can be pushed to the [`service.data-gateway`](../data-gateway).

## Protocols

Available protocols can be found under the [Methods](./Methods) directory. Each protocol contains a README documenting the required spec to trigger it.

Examples of protocol triggers for the `service.tecan-spark-relay` can be found under [`protocols/examples/tecan-spark-relay`](../../protocols/examples/tecan-spark-relay).

## Data Export

The `service.tecan-spark-relay` forwards data produced by the Spark® to the `service.data-gateway` in the following format:

```json
{
  "timeElapsed": "time elapsed",
  "error": "error",
  "absorbance": "absorbance"
}
```

## Development

#### Adding New Protocols