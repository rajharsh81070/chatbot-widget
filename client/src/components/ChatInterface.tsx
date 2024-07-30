import React, { useState, useEffect } from "react";
import { startSession, createMessage, editMessage } from "../services/api";
import { Dialog, DialogPanel } from "@headlessui/react";
import { Message } from "../types";
import InputArea from "./InputArea";
import { AgentChatMessage } from "./ChatMessage";
import { AvaIntroduction } from "./Ava";

const ChatInterface: React.FC = () => {
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const [isEditing, setIsEditing] = useState<boolean>(false);

  useEffect(() => {
    const initSession = async () => {
      const id = await startSession();
      setSessionId(id);
      setMessages([
        {
          id: 1,
          content: "Hi, I'm Ava. How can I help you today?",
          is_from_user: false,
          created_at: new Date().toISOString(),
          session_id: id,
          updated_at: new Date().toISOString(),
        },
      ]);
    };
    initSession();
  }, []);

  const handleSendMessage = async () => {
    if (inputMessage.trim() && sessionId) {
      setInputMessage("");

      const response = await createMessage(inputMessage);
      setMessages((prevMessages) => [...prevMessages, ...response]);
    }
  };

  return (
    <div className="w-full h-full">
      <div
        className="flex items-center cursor-pointer justify-center fixed bottom-5 right-4 h-14 w-14 bg-purple-300 rounded-full"
        onClick={() => setIsOpen(true)}
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          className="size-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 0 1 .865-.501 48.172 48.172 0 0 0 3.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z"
          />
        </svg>
      </div>
      <Dialog
        open={isOpen}
        onClose={() => setIsOpen(false)}
        className="relative z-50"
      >
        <div className="fixed bottom-20 right-4 flex w-[400px] h-[600px] overflow-y-auto items-center justify-center p-4">
          <DialogPanel className="border border-solid border-gray-100 bg-white p-3 w-full h-full overflow-y-auto rounded-2xl">
            <div className="w-full h-full flex justify-center items-center">
              <div className="flex gap-1 flex-col overflow-auto h-full w-full">
                <div className="flex-1 gap-2 flex-col flex w-full">
                  <div className="w-full flex flex-row-reverse">
                    <div
                      className="cursor-pointer"
                      onClick={() => setIsOpen(false)}
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        strokeWidth={1.5}
                        stroke="currentColor"
                        className="size-6"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          d="M6 18 18 6M6 6l12 12"
                        />
                      </svg>
                    </div>
                  </div>
                  <div className="flex flex-col justify-center items-center gap-8">
                    <div className="flex flex-col gap-3 w-full h-full">
                      <AvaIntroduction />
                      {messages.map((message) =>
                        message.is_from_user ? (
                          <div
                            key={message.id}
                            className="flex w-full flex-row-reverse"
                          >
                            <div className="flex w-fit min-w-20 items-start p-2 bg-purple-400 rounded-lg">
                              {!isEditing ? (
                                <div className="flex justify-end">
                                  <p className="text-sm text-gray-600">
                                    {message.content}
                                  </p>
                                </div>
                              ) : (
                                <InputArea
                                  value={message.content}
                                  onChange={async (e) => {
                                    const newMessage = await editMessage(
                                      message.id,
                                      e.target.value
                                    );

                                    setMessages((prevMessages) =>
                                      prevMessages.map((msg) =>
                                        msg.id === message.id ? newMessage : msg
                                      )
                                    );
                                  }}
                                  onSend={() => setIsEditing(false)}
                                  showImage={false}
                                />
                              )}
                            </div>
                          </div>
                        ) : (
                          <AgentChatMessage
                            key={message.id}
                            message={message.content}
                            avatarSrc="/assets/ava.svg"
                          />
                        )
                      )}
                    </div>
                  </div>
                </div>
                <div className="flex-0 flex-col flex w-full gap-2">
                  <hr className="w-full text-grey-100" />
                  <InputArea
                    value={inputMessage}
                    onChange={(e) => setInputMessage(e.target.value)}
                    onSend={handleSendMessage}
                  />
                </div>
              </div>
            </div>
          </DialogPanel>
        </div>
      </Dialog>
    </div>
  );
};

export default ChatInterface;
