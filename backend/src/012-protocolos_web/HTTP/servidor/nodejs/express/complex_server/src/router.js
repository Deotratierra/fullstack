
const router = require("express").Router();

import { info } from "./utils/printers";

router.use( (req, res, next) => {
    info(req.method + " " + req.url);
    next();
});



router.use("/admin", require("./scenes/admin/router"));

module.exports = router;