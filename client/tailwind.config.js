/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        violet: {
          400: '#8B5CF6',
          500: '#7C3AED',
          600: '#6D28D9',
        },
        purple: {
          300: '#D8B4FE',
          400: '#C084FC',
        },
      },
    },
  },
  plugins: [],
}

