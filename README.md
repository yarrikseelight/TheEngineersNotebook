# 📝 The Engineers Notebook  

Built while learning the basics of Django in 2022-2023:  

✨ **Key Features**:  
- 🖥️ **Views & URLs**: Dynamic routing with Django!  
- 🛠️ **Models**: Structured data for blog posts.  
- 🔑 **User Authentication**: Login, logout & registration.  
- 📝 **DTL** (Django Template Language): For rendering pages beautifully.  
- 💬 **Commenting System**: Engage with posts.
- 🔧 **Django Admin Panel**: Manage blog posts, comments, and users easily!  


## 🐳 Docker Image
⚠️ This Docker image is built for **development / demo purposes only**.

- Docker Hub:
 [jereseilo/engineersnotebook](https://hub.docker.com/repository/docker/jereseilo/engineersnotebook/general)
```bash
docker run -p 8000:8000 jereseilo/engineersnotebook:demo
```

- To build locally:

```bash
docker build -t TheEngineersNotebook .
docker run -p 8000:8000 TheEngineersNotebook
