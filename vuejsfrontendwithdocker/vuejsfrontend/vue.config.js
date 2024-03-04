const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      "/api": {
        target: "http://172.18.0.2:5000",
        pathRewrite: { "^/api": "" },
      },
    },
  },
});