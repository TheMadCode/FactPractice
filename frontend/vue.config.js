module.exports = {
    devServer: {
      proxy: {
        '^/human.api': {
          target: 'http://localhost:5050',
          changeOrigin: true
        },
      }
    }
  }