// /** @type {import('next').NextConfig} */
// const nextConfig = {};

// export default nextConfig;

/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    async rewrites() {
      return [
        {
          source: '/analyze',
          destination: 'http://localhost:5000/analyze', // Asume que Flask está corriendo en el puerto 5000
          // destination: 'https://tu-backend-flask.herokuapp.com/analyze', // Ajusta esta URL
          // destination: '/analyze', // Esto sigue apuntando a la ruta del backend
        },
      ]
    },
    // Asegúrate de que el output sea 'standalone' para Vercel
    output: 'standalone',
}
  
  export default nextConfig;