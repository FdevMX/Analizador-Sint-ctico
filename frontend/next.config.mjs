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
          destination: '/analyze', // Esto sigue apuntando a la ruta del backend
        },
      ]
    },
    // Asegúrate de que el output sea 'standalone' para Vercel
    output: 'server',
}
  
  export default nextConfig;