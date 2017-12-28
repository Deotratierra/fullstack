import path from "path";
const admin_router = require("express").Router();

admin_router.get("/home", (req, res) => {
    res.sendFile( path.join(__dirname, "Home", "index.html") );
});

module.exports = admin_router;