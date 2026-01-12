# 📝 The Engineers Notebook  

Built while learning the basics of Django in 2022-2023:  

✨ **Key Features**:  
- 🖥️ **Views & URLs**: Dynamic routing with Django!  
- 🛠️ **Models**: Structured data for blog posts.  
- 🔑 **User Authentication**: Login, logout & registration.  
- 📝 **DTL** (Django Template Language): For rendering pages beautifully.  
- 💬 **Commenting System**: Engage with posts.
- 🔧 **Django Admin Panel**: Manage blog posts, comments, and users easily!

✨ **Key Things Learned**:  
- 🐍 **Django Fundamentals**: Gained hands-on experience with a web development framework and learnt how Django uses MTV (model-template-view) architecture and how it handles different backend tasks. 
- 🌐 **Web Development Basics**: Learnt basic flow of web application, including things such as requests, routing, datamodels, and dynamic templates.  
- 🔐 **Authentication and Authorization**: Implemented user registration and login, and learnt how protected routes work as well as how authentication and authorization are implemented.  
- 🗄️ **Models and Databases** Built models to represent data, learned Django ORM basics, and performed CRUD operations (Create, Read, Update, Delete).
- 📝 **Forms and Validation**: Created forms for user comments, added validation, and handled comment submissions safely.
- 🔧 **Project Structure & Best Practices**: Learned how to structure a Django project, organize apps, and follow basic conventions for maintainability. 


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
