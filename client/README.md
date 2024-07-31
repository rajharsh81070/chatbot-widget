# Chat Widget Frontend

## Table of Contents

- [Chat Widget Frontend](#chat-widget-frontend)
  - [Table of Contents](#table-of-contents)
  - [Tech Stack](#tech-stack)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [Building for Production](#building-for-production)
  - [Running Tests](#running-tests)
  - [Project Structure](#project-structure)

## Tech Stack

- React 18+
- TypeScript
- Vite (for build tooling)
- Tailwind CSS
- Axios (for API requests)
- Headless UI (for accessible UI components)
- Hero Icons

## Getting Started

### Prerequisites

- Node.js 14.0 or higher
- npm or yarn

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/rajharsh81070/chatbot-widget.git
   cd chatbot-widget/client
   ```

2. Install dependencies:
   ```
   npm install
   # or
   yarn install
   ```

## Running the Application

To run the application in development mode:

```
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:5173`.

## Building for Production

To build the application for production:

```
npm run build
# or
yarn build
```

The built files will be in the `dist` directory.


## Project Structure

```
src/
├── components/
│   ├── ChatInterface.tsx
│   ├── Ava.tsx
│   ├── ActionButton.tsx
│   ├── InputArea.tsx
│   └── ChatMessage.tsx
├── services/
│   └── api.ts
├── types.ts
├── constant.ts
├── App.tsx
└── main.tsx
```

- `components/`: Contains all React components
- `services/`: Contains API service functions
- `types/`: Contains TypeScript type definitions
- `constants/`: Contains constant values used across the application

## Docker

To build and run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t chat-widget-frontend .
   ```

2. Run the container:
   ```
   docker run -p 5173:5173 chat-widget-frontend
   ```

The application will be available at `http://localhost:5173`.
