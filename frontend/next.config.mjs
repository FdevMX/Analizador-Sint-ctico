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
        },
      ]
    },
    // Asegúrate de que el output sea 'standalone' para Vercel
    output: 'standalone',
}
  
  export default nextConfig;