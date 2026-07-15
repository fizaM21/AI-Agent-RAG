import * as React from "react"

import { cn } from "@/lib/utils"

interface MessageProps extends React.HTMLAttributes<HTMLDivElement> {
  author: "user" | "assistant"
  content: string
}

function Message({ author, content, className, ...props }: MessageProps) {
  const isUser = author === "user"

  return (
    <div
      className={cn(
        "flex w-full gap-3 px-2",
        isUser ? "justify-end" : "justify-start",
        className
      )}
      {...props}
    >
      {!isUser && (
        <div className="flex items-end">
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-slate-200 text-sm font-semibold text-slate-700 shadow-sm">
            AI
          </div>
        </div>
      )}

      <div className="max-w-[90%] sm:max-w-[70%]">
        <div
          className={cn(
            "rounded-[1.75rem] px-5 py-4 text-sm leading-7 shadow-sm transition duration-200",
            isUser
              ? "bg-slate-950 text-white shadow-slate-900/10"
              : "bg-white text-slate-900 border border-slate-200 shadow-slate-200/50"
          )}
        >
          {content}
        </div>
      </div>

      {isUser && (
        <div className="flex items-end">
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-slate-950 text-sm font-semibold text-white shadow-sm">
            Y
          </div>
        </div>
      )}
    </div>
  )
}

export { Message }
