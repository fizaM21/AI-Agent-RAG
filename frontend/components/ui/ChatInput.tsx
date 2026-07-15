"use client"

import * as React from "react"

import { Textarea } from "@/components/ui/textarea"
import { cn } from "@/lib/utils"

interface ChatInputProps {
  value: string
  onChange: (value: string) => void
  onSend: () => void
  isSending?: boolean
}

function ChatInput({ value, onChange, onSend, isSending }: ChatInputProps) {
  return (
    <form
      className="grid gap-3 sm:grid-cols-[1fr_auto]"
      onSubmit={(event) => {
        event.preventDefault()
        if (!isSending && value.trim().length > 0) {
          onSend()
        }
      }}
    >
      <Textarea
        value={value}
        onChange={(event) => onChange(event.target.value)}
        placeholder="Type your message here..."
        disabled={isSending}
        onKeyDown={(event: React.KeyboardEvent<HTMLTextAreaElement>) => {
          if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault()
            if (!isSending && value.trim().length > 0) {
              onSend()
            }
          }
        }}
        className={cn(
          "min-h-[5rem] rounded-[1.75rem] border border-slate-200 bg-slate-100 px-4 py-3 text-sm text-slate-950 shadow-sm outline-none transition duration-200 ease-in-out focus:border-slate-400 focus:ring-2 focus:ring-slate-300/60 disabled:cursor-not-allowed disabled:bg-slate-100/80",
          value.length === 0 && "placeholder:text-slate-400"
        )}
      />

      <button
        type="submit"
        className="inline-flex h-12 items-center justify-center gap-2 rounded-[1.5rem] bg-slate-950 px-6 text-sm font-semibold text-white transition duration-200 ease-in-out hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-50 disabled:bg-slate-700"
        disabled={isSending || value.trim().length === 0}
      >
        {isSending ? (
          <>
            <span className="inline-block h-4 w-4 animate-spin rounded-full border-2 border-white/30 border-t-white" />
            Sending...
          </>
        ) : (
          "Send"
        )}
      </button>
    </form>
  )
}

export { ChatInput }
