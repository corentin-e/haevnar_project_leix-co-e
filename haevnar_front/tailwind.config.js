/** @type {import('tailwindcss').Config} */

export default {
  content: [],
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false,
  theme: {
    extend: {},
    colors: {
      haev_black: '#000000',
      haev_blue: '#2D72A4',
      haev_dark: '#323436',
      haev_orange: '#F77C04',
      haev_white: '#E4E4E4',
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

