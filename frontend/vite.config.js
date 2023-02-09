import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";

// const path = require('path')

// export default {
//   root: path.resolve(__dirname, 'src'),
//   server: {
//     port: 8080,
//     hot: true
//   }
// }

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 80,
    hot: true
  },

  plugins: [vue(), vueJsx()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
    devServer: {
      proxy: {
        '^/': {
          target: 'http://localhost:5050',
          changeOrigin: true
        },
      }
    }
});
