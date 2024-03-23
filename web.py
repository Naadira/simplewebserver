from http.server import HTTPServer,BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <title>Saveetha Home Page</title>
<style>
*
{
    box-sizing: border-box;
}
body{
    margin:0;
    background-color:wheat;
}
.first-part
{
    background-color: gray;
    width: 100%;
    border:solid 1px black;
    padding:1.5%;
}

.second-part
{
    padding:4%;
    padding:2%;
    margin-left:1%;
    background-color: white;
    border-radius: 15px;
}

#part
{
    font-size: 105%;
}

.aside
{
    
    width:30%;
    margin:1% 0% 0% 1%;
    background-color: rgb(205, 78, 78);
    padding:2%;
    align-items: center;
}
button{
    background-color: white;
   padding:3%;
}
#text
{
    color:white;
    padding:3%;
    font-size: 30px;
}
</style>   

</head>
<body>
    <div class="row" style="background-color:#f3f3f3">
        <div class="col-5">
            <a href=""><i class="bi bi-twitter"></i></a>
            <a href=""><i class="bi bi-youtube"></i></a>
            <a href=""><i class="bi bi-facebook"></i></a>
            <a href=""><i class="bi bi-linkedin"></i></a>
            <a href=""><i class="bi bi-pinterest"></i></a>
            <a href=""><i class="bi bi-whatsapp"></i></a>
            <a href=""><i class="bi bi-instagram"></i></a>
          </div>
        <div class="col-4 "> 
            <a href="">Alumni</a><i class="bi bi-three-dots-vertical"></i></a>
            <a href="">Event</a><i class="bi bi-three-dots-vertical"></i></a>
            <a href="">Career</a><i class="bi bi-three-dots-vertical"></i></a>
            <a href="">Login</a><i class="bi bi-three-dots-vertical"></i></a>
            <a href="">SEC portal</a>
          </div>
        <div class="col-3">
             <div style="border: 2px solid;border-radius: 15px">
                <i class="bi bi-search"></i>
                <input type="text" placeholder="search" style="background-color: #f3f3f3;border:0px; outline: none;"/>
            </div>
       </div>
    </div>
    <div class="row m-2" >
        <div class="col-4">
            <img src="assets/images/logo.png" width="450px">
        </div>
        <div class="col-6">
          <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
              
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="#">About</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="#">Departments</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="#">Life at SEC</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="#">Admissions</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="#">Placements</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="#">Research</a>
                  </li>
                </ul>  
              </div>
            </div>
          </nav>
        </div>
        <div class="col-2  border-2">
          <div style="width:100%; align-items:right; background-color: gray;">
            <p> FOR ADMISSION <br>
             <i class="bi bi-whatsapp"></i> 9876544678</p>
        </div>
        </div>
    </div>
    <div style="display:flex;">
      <div class="aside" style="width:20%; height:600px;">
          <p id="text">ADMISSION ENQUIRY</p>
          <button>APPLY NOW</button>
          <hr>
          <br>
          <p id="text">Chat with Student Ambassador </p>
          <button>KNOW MORE</button>
          <hr>
          <br>
          <p id="text">BLOGS</p>
          <button>KNOW MORE</button>
          <hr>
        
      </div>

    <div id="carouselExampleIndicators" class="carousel slide" >
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="assets/images/nature1.jpg" class="d-block w-100" height="auto" alt="...">
        </div>
        <div class="carousel-item">
          <img src="assets/images/nature2.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="assets/images/nature3.jpeg" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    
</div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
"""
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("my webserver is running...") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
