const express = require("express");

const app = express();

const PORT = 4000;

app.listen(PORT, () => {
  console.log("app is listening to port: " + PORT);
});

// Function to serve all static files
// inside Tiles directory.
app.use(express.static("Tiles"));
app.use("/Tiles", express.static("Tiles"));
