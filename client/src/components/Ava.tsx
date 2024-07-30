import React from "react";

export const AvaIntroduction: React.FC = () => {
  return (
    <div className="flex flex-col items-center">
      <img
        src="/assets/ava.svg"
        alt="Ava Avatar"
        className="rounded-full w-[42px] h-[42px]"
      />
      <div className="flex items-center mt-2 font-semibold">
        <span className="text-xs text-gray-700">Hey &nbsp;</span>
        <span>
          <img src="/assets/hand.svg" alt="Hand" />
        </span>
        &nbsp;
        <span className="text-xs text-gray-700">I'm Ava</span>
      </div>
      <p className="mt-1 text-xs font-semibold text-gray-400">
        Ask me anything or pick a place to start
      </p>
    </div>
  );
};
