# Copilot Instructions for the Interviews Codebase

## Overview
This codebase is structured to facilitate interviews related to SRE/DevOps, with a focus on Docker and Kubernetes. Understanding the architecture and workflows is crucial for effective contributions.

## Architecture
- **Major Components**: The primary components include Docker, Kubernetes, and various scripts for managing deployments and configurations. Each component interacts with others through defined interfaces, primarily using Docker containers and Kubernetes manifests.
- **Service Boundaries**: Services are encapsulated within Docker containers, allowing for isolated environments. Kubernetes orchestrates these containers, managing scaling and networking.
- **Data Flows**: Data flows between services via defined APIs and shared volumes. Understanding these flows is essential for debugging and enhancing functionality.

## Developer Workflows
- **Building**: Use the `Dockerfile` in the `webapp/` directory to build images. The command is `docker build -t <image-name> .` from the `webapp/` directory.
- **Testing**: Tests are typically run within the Docker containers. Use `docker-compose` to spin up the necessary services for integration tests.
- **Debugging**: Utilize `kubectl logs <pod-name>` to view logs for debugging. Familiarize yourself with common commands like `kubectl get pods` and `kubectl describe pod <pod-name>` for troubleshooting.

## Project-Specific Conventions
- **Naming Conventions**: Follow the established naming conventions for Docker images and Kubernetes resources. Use lowercase letters and hyphens for image names.
- **Configuration Management**: Configuration files are stored in the `webapp/` directory. Ensure that any changes to configurations are documented in the README files.

## Integration Points
- **External Dependencies**: The project relies on Docker Hub for image storage and Kubernetes for orchestration. Ensure you have access to these services.
- **Cross-Component Communication**: Services communicate over defined ports. Ensure that your local environment mirrors the production setup for accurate testing.

## Key Files/Directories
- **Dockerfile**: Located in `webapp/`, this file defines how to build the application image.
- **Kubernetes Manifests**: Found in the `webapp/` directory, these YAML files define the deployment and service configurations.
- **README.md**: The main documentation file that provides an overview of the project and its components.

## Conclusion
Familiarize yourself with the above components and workflows to effectively contribute to this codebase. For any unclear sections, please provide feedback for further clarification.