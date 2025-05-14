# 📝 The Engineers Notebook  

Built while learning the basics of Django:  

✨ **Key Features**:  
- 🖥️ **Views & URLs**: Dynamic routing with Django!  
- 🛠️ **Models**: Structured data for blog posts.  
- 🔑 **User Authentication**: Login, logout & registration.  
- 📝 **DTL** (Django Template Language): For rendering pages beautifully.  
- 💬 **Commenting System**: Engage with posts.
- 🔧 **Django Admin Panel**: Manage blog posts, comments, and users easily!  


## 🐳 Docker Image

- Docker Hub: [jereseilo/engineersnotebook](https://hub.docker.com/repository/docker/jereseilo/engineersnotebook/general)
- To build locally:

```bash
docker build -t TheEngineersNotebook .
docker run -p 8000:8000 TheEngineersNotebook
