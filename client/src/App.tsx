import React from "react";
import ChatInterface from "./components/ChatInterface";

const App: React.FC = () => {
  return (
    <div className="flex justify-center items-center min-h-screen w-full bg-gray-100">
      <ChatInterface />
    </div>
  );
};

export default App;
