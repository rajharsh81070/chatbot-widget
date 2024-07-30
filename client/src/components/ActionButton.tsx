import React from "react";

interface ActionButtonProps {
  text: string;
  onClick?: () => void;
}

const ActionButton: React.FC<ActionButtonProps> = ({ text, onClick }) => {
  return (
    <div className="flex flex-col justify-center px-1.5 py-1 text-xs text-violet-400 bg-black bg-opacity-0">
      <button
        onClick={onClick}
        className="py-2.5 bg-white rounded-lg border border-purple-400 border-solid"
      >
        {text}
      </button>
    </div>
  );
};

export default ActionButton;
