const path = require('path');
const webpack = require('webpack');


const NODE_ENV = (process.env.NODE_ENV == "stage") ? "production" : process.env.NODE_ENV;

console.log("Bundling on " + NODE_ENV + " environment...");

module.exports = {
   mode: NODE_ENV,
   watch: (NODE_ENV == "development") && process.argv.includes("--watch"),
   devtool: (NODE_ENV == "development") ? "source-maps" : "eval",
   entry: {
     external: path.resolve(__dirname, "web", "static", "src", "external.js"),
     internal: path.resolve(__dirname, "web", "static", "src", "internal.js"),
   },
   output: {
     // Esta es la salida del bundle, que será guardada en el directorio especificado en `path`
     filename: "[name].bundle.js",
     path: path.resolve(__dirname, "web", "static", "dist", "js")
   },
   module: {
    rules: [
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      },
      {
        test: /\.(scss)$/,
        use: [{
          loader: 'style-loader', // inject CSS to page
        }, {
          loader: 'css-loader', // translates CSS into CommonJS modules
        }, {
          loader: 'postcss-loader', // Run post css actions
          options: {
            plugins: function () { // post css plugins, can be exported to postcss.config.js
              return [
                require('precss'),
                require('autoprefixer')
              ];
            }
          }
        }, {
          loader: 'sass-loader' // compiles Sass to CSS
        }]
      },
      {
        test: /\.js$/,
        use: ["source-map-loader"],
        enforce: "pre"
      },
      {
        test: /\.(png|woff|woff2|eot|ttf|svg)$/,
        use: "url-loader?limit=100000"
      }
    ]
  },
  plugins: [
    new webpack.ProgressPlugin()
  ]
};
