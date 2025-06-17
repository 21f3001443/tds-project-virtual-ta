## Containers: Docker, Podman

[Docker](https://www.docker.com/) and [Podman](https://podman.io/) are containerization tools that package your application and its dependencies into a standardized unit for software development and deployment.

Docker is the industry standard. Podman is compatible with Docker and has better security (and a slightly more open license). In this course, we recommend Podman but Docker works in the same way.

Initialize the container engine:

```bash
podman machine init
podman machine start
```

Common Operations. (You can use `docker` instead of `podman` in the same way.)

```bash
# Pull an image
podman pull python:3.11-slim

# Run a container
podman run -it python:3.11-slim

# List containers
podman ps -a

# Stop container
podman stop container_id

# Scan image for vulnerabilities
podman scan myapp:latest

# Remove container
podman rm container_id

# Remove all stopped containers
podman container prune
```

You can create a `Dockerfile` to build a container image. Here's a sample `Dockerfile` that converts a Python script into a container image.

```dockerfile
FROM python:3.11-slim
# Set working directory
WORKDIR /app
# Typically, you would use `COPY . .` to copy files from the host machine,
# but here we're just using a simple script.
RUN echo 'print("Hello, world!")' > app.py
# Run the script
CMD ["python", "app.py"]
```

To build, run, and deploy the container, run these commands:

```bash
# Create an account on https://hub.docker.com/ and then login
podman login docker.io

# Build and run the container
podman build -t py-hello .
podman run -it py-hello

# Push the container to Docker Hub. Replace $DOCKER_HUB_USERNAME with your Docker Hub username.
podman push py-hello:latest docker.io/$DOCKER_HUB_USERNAME/py-hello

# Push adding a specific tag, e.g. dev
TAG=dev podman push py-hello docker.io/$DOCKER_HUB_USERNAME/py-hello:$TAG
```

Tools:

- [Dive](https://github.com/wagoodman/dive): Explore image layers
- [Skopeo](https://github.com/containers/skopeo): Work with container images
- [Trivy](https://github.com/aquasecurity/trivy): Security scanner

[![Podman Tutorial Zero to Hero | Full 1 Hour Course](https://i.ytimg.com/vi_webp/YXfA5O5Mr18/sddefault.webp)](https://youtu.be/YXfA5O5Mr18
<youtube_summary>This comprehensive tutorial introduces Podman, an open-source, daemonless container management tool similar to Docker but with unique features like rootless container execution for enhanced security. Podman supports running containers in pods (groups of containers sharing resources), inspired by Kubernetes, and can export these pods as Kubernetes manifests. The tutorial covers installing Podman on Ubuntu, macOS (using Homebrew), and Windows (via executable), highlighting that on non-Linux systems, Podman uses a Linux virtual machine to run containers.

Users learn to configure container registries through a registry configuration file, enabling interaction with various registries like Docker Hub, GitHub Container Registry, Red Hat, or private registries. The tutorial explains essential Podman commands for searching, pulling, running, listing, stopping, and removing containers and images, emphasizing that Podman commands mirror Docker’s but run without root privileges.

It guides users through creating and running containers from popular images (e.g., BusyBox, Nginx) and building custom container images using Dockerfiles, demonstrated with a Go application exposing a simple web service. The process includes writing the Go application, containerizing it with a Dockerfile based on Alpine Linux, building the image, running the container, and pushing the image to Docker Hub after tagging it appropriately. Pulling and running the image from the registry is also shown.

Podman’s pod management is detailed, showing how to create pods, add containers to pods, and manage pods with commands like podman pod create, ls, start, stop, and rm. The concept of an infra container, automatically added to pods to manage shared namespaces, is explained. The tutorial also covers generating Kubernetes YAML manifests from Podman pods and running pods locally from these manifests using podman generate kube and podman play kube commands, facilitating local testing of Kubernetes configurations.

Lastly, the tutorial introduces Podman Desktop, a user-friendly graphical interface available for Windows, macOS, and Linux. It demonstrates installing Podman Desktop, managing Podman installations within it, and using its dashboard, container, pod, image, and volume views. Users learn to pull and build images, create and run containers and pods, inspect logs, access terminals inside containers, generate Kubernetes manifests, and manage volumes—all through the GUI. Settings for managing Podman machines, proxies, and registries are also covered.

Throughout, best practices and tips are shared, such as avoiding naming conflicts by not specifying container names manually and using the RM option to clean up containers after use. The tutorial concludes by encouraging viewers to subscribe for more content, marking the completion of a thorough Podman learning journey from beginner to advanced usage.</youtube_summary>
)

[![Learn Docker in 7 Easy Steps - Full Beginner's Tutorial](https://i.ytimg.com/vi_webp/gAkwW2tuIqE/sddefault.webp)](https://youtu.be/gAkwW2tuIqE
<youtube_summary>This video addresses imposter syndrome among developers caused by not knowing Docker, especially when discussing technologies like Kubernetes. It provides a beginner-friendly, hands-on guide to Docker, starting from installation to advanced concepts.

Key points covered:

1. **What is Docker?**  
   Docker packages software to run consistently across different hardware by using Dockerfiles (blueprints), images (immutable snapshots), and containers (running instances). It solves environment inconsistencies by allowing developers to define and reproduce environments exactly.

2. **Installation and Tooling:**  
   - Recommended Docker Desktop for Mac/Windows for CLI and GUI.  
   - Install Docker extension for VS Code or other IDEs for language support and integration.

3. **Dockerfile Basics:**  
   - Uses instructions like FROM (base image), WORKDIR (set working directory), COPY (copy files), RUN (execute commands), ENV (set environment variables), EXPOSE (declare ports), and CMD (run app).  
   - Uses official Node.js base image for a Node.js app.  
   - Demonstrates layering and caching to optimize builds, installing dependencies before copying source code to avoid reinstalling node_modules unnecessarily.  
   - Uses .dockerignore file to exclude local node_modules from being copied.

4. **Building and Running Images:**  
   - Build images with `docker build -t username/appname:version .`  
   - Run containers with `docker run`, using `-p` flag for port forwarding (e.g., `-p 5000:8080`) to expose container ports to the host.  
   - Notes containers keep running after terminal closes; management via Docker Desktop GUI.

5. **Data Persistence and Sharing:**  
   - Introduces volumes as persistent storage shared across containers using `docker volume create` and mounting volumes at runtime.

6. **Debugging and Inspection:**  
   - Use Docker Desktop to view logs and open CLI inside containers.  
   - Alternatively use `docker exec` to interact with running containers.

7. **Best Practices:**  
   - Keep containers focused on one process; use multiple containers for multi-process apps.

8. **Docker Compose for Multi-Container Apps:**  
   - Defines multiple containers and volumes in a `docker-compose.yaml` file.  
   - Example: a Node.js app with a MySQL database and volume for data persistence.  
   - Use `docker compose up` to start all containers and `docker compose down` to stop them easily.

The video encourages hands-on practice with the provided source code and highlights the value of Docker for modern development, especially in scaling and managing applications. It concludes by inviting viewers to like, subscribe, and consider advanced courses using Docker.</youtube_summary>
)

- Optional: For Windows, see [WSL 2 with Docker getting started](https://youtu.be/5RQbdMn04Oc
<youtube_summary>The video demonstrates how to install Docker on a Windows 10 laptop using WSL version 2. The presenter references a previous video showing how to install WSL 2 and uses Docker's official documentation from docs.docker.com/docker-for-windows/wsl/. Key prerequisites include running Windows 10 version 2004 or higher (Windows Home edition is sufficient), enabling WSL 2 by turning on the "Windows Hypervisor Platform" and "Windows Subsystem for Linux" features, and installing the Linux kernel update package.

After meeting prerequisites, the user downloads Docker Desktop Stable release (about 391 MB), runs the installer, and configures it to use WSL 2 (mandatory for Windows Home, as Hyper-V is unsupported). Post-installation, Docker Desktop starts with a WSL 2 backend. The user verifies their default WSL distro via PowerShell commands (wsl -l -v) and enables Docker integration with the default distro in settings.

The presenter runs Docker commands within the Ubuntu 2004 LTS WSL distro, showing Docker pulling and running containers like "hello-world" and an Ubuntu container. Inside the Docker Ubuntu container, some commands like "lsb_release -a" initially do not work until the user updates package references and installs lsb-release. They demonstrate exiting from the Docker container back to the Ubuntu VM, then exiting back to Windows, highlighting the nesting of operating systems: Windows runs WSL 2 (Ubuntu VM), which runs Docker, which runs an Ubuntu container.

Overall, the video thoroughly explains installing Docker on Windows 10 Home with WSL 2, configuring integration, running containers, and understanding the layered virtualization environment.</youtube_summary>
)
