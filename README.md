<div style="color: black; background-color: #edf497;">
    <img src="./assets/images/uncertainty-engine-logo.png">
</div>

# Types

Common types definitions for the Uncertainty Engine.
This library should be used by other packages to ensure consistency in the types used across the Uncertainty Engine.

## Overview

### Execution & Error Handling

- **ExecutionError**  
  Exception raised to indicate execution errors.

### Graph & Node Types

- **Graph**  
  Represents a collection of nodes and their connections.
- **NodeElement**  
  Defines a node with a type and associated inputs.
- **NodeId**  
  A unique identifier for nodes.
- **SourceHandle** & **TargetHandle**  
  Strings used to reference node connections.

### Node Handles

- **Handle**  
  Represents a node handle in the format `node.handle` and validates this structure.

### Language Learning Models (LLMs)

- **LLM**  
  Abstract base class for language learning models.
- **OpenAILLM**  
  LLM implementation using OpenAI.
- **OllamaLLM**  
  LLM implementation using Ollama.
- **LLMProvider**  
  Enum listing supported LLM providers.
- **LLMManager**  
  Manages connections to LLMs based on the chosen provider and configuration.

### Messaging

- **Message**  
  Represents a message with a role and content, used for interactions with LLMs.

### TwinLab Models

- **TwinLabModel**  
  Represents a model configuration including metadata.
- **save_model**  
  Function to persist a model configuration.

### Node Metadata

- **NodeInputInfo**  
  Describes the properties of a node's input.
- **NodeOutputInfo**  
  Describes the properties of a node's output.
- **NodeInfo**  
  Aggregates metadata for a node, including inputs and outputs.

### Sensor Design

- **SensorDesigner**  
  Defines sensor configuration and provides functionality to load sensor data.
- **save_sensor_designer**  
  Function to persist a sensor designer configuration.

### SQL Database Types

- **SQLDatabase**  
  Abstract base class for executing SQL queries.
- **PostgreSQL**  
  Implementation of SQLDatabase for PostgreSQL.
- **SQLKind**  
  Enum listing supported SQL database types.
- **SQLManager**  
  Manages connections and operations for SQL databases.

### Tabular Data

- **TabularData**  
  Represents CSV-based data and includes functionality to load it into a pandas DataFrame.

### Token Types

- **Token**  
  Enum representing token types, such as TRAINING and STANDARD.

### Vector Stores

- **VectorStoreConnection**  
  Abstract base class for vector store operations.
- **WeaviateVectorStoreConnection**  
  Implements a connection to a Weaviate vector store.
- **VectorStoreProvider**  
  Enum for supported vector store providers.
- **VectorStoreManager**  
  Manages connections to vector stores.
- **get_persistent_vector_store**  
  Function to establish a persistent connection to a Weaviate vector store.
- **get_embedding_function**  
  Retrieves an embedding function based on configuration, supporting both HuggingFace and OpenAI options.
