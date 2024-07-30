import React from "react";

interface InputAreaProps {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  onSend: () => void;
  showImage?: boolean;
}

const InputArea: React.FC<InputAreaProps> = ({
  value,
  onChange,
  onSend,
  showImage = true,
}) => {
  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      onSend();
    }
  };

  return (
    <div className="flex items-center justify-center gap-2 py-3 bg-black bg-opacity-0">
      {showImage && (
        <img
          loading="lazy"
          src="/assets/input-image.svg"
          alt=""
          className="shrink-0 rounded-xl aspect-square w-[26px]"
        />
      )}
      <input
        type="text"
        value={value}
        onChange={onChange}
        onKeyPress={handleKeyPress}
        placeholder="Your question"
        className="flex-auto my-auto text-black bg-transparent focus:outline-none"
      />
      <div className="cursor-pointer" onClick={onSend}>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          className="size-5"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5"
          />
        </svg>
      </div>
    </div>
  );
};

export default InputArea;
