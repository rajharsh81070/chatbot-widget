import React from "react";

interface ChatMessageProps {
  avatarSrc: string;
  message: string;
}

export const AgentChatMessage: React.FC<ChatMessageProps> = ({
  avatarSrc,
  message,
}) => {
  return (
    <div className="flex gap-2 px-4 pt-2 pb-1 font-semibold">
      <img
        src={avatarSrc}
        alt="User avatar"
        className="shrink-0 self-start rounded-2xl w-[24px] h-[24px]"
      />
      <div className="flex flex-col grow items-start p-2 bg-gray-50 rounded-lg">
        <span className="text-sm text-gray-600">{message}</span>
      </div>
    </div>
  );
};
