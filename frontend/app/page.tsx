"use client"

import { useEffect, useRef, useState, type ChangeEvent } from "react"
import { ChatInput } from "@/components/ui/ChatInput"
import { Message } from "@/components/ui/Message"
import { Navbar } from "@/components/ui/Navbar"
import { UploadButton } from "@/components/ui/UploadButton"
import api from "@/lib/api"

const initialMessages = [
  {
    author: "assistant" as const,
    content: "Hi there! I�m your AI Agent UI. Start typing below to begin a conversation.",
  },
]

export default function Home() {
  const [query, setQuery] = useState("")
  const [messages, setMessages] = useState(initialMessages)
  const [isSending, setIsSending] = useState(false)
  const [uploadStatus, setUploadStatus] = useState<"" | "success" | "error">("")
  const [uploadMessage, setUploadMessage] = useState("")
  const fileInputRef = useRef<HTMLInputElement | null>(null)
  const messagesEndRef = useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages])

  async function handleSend() {
    const trimmed = query.trim()
    if (!trimmed) {
      return
    }

    setIsSending(true)
    setMessages((current) => [...current, { author: "user", content: trimmed }])
    setQuery("")

    try {
      const response = await api.post("/chat", { query: trimmed })
      const answer = response.data?.answer ?? "No answer returned."
      setMessages((current) => [
        ...current,
        {
          author: "assistant",
          content: answer,
        },
      ])
    } catch (error) {
      setMessages((current) => [
        ...current,
        {
          author: "assistant",
          content: "Sorry, there was a problem reaching the backend.",
        },
      ])
    } finally {
      setIsSending(false)
    }
  }

  async function handleUpload(file: File) {
    const formData = new FormData()
    formData.append("file", file)

    try {
      const response = await api.post("/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      })

      setUploadStatus("success")
      setUploadMessage(response.data?.message ?? "PDF uploaded successfully.")
    } catch (error) {
      setUploadStatus("error")
      setUploadMessage("Failed to upload PDF. Please try again.")
    }
  }

  function triggerUpload() {
    fileInputRef.current?.click()
  }

  async function onFileChange(event: ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0]
    if (!file) {
      return
    }

    if (file.type !== "application/pdf") {
      setUploadStatus("error")
      setUploadMessage("Please select a valid PDF file.")
      return
    }

    await handleUpload(file)
    event.target.value = ""
  }

  return (
    <div className="flex min-h-screen flex-col bg-slate-100 text-slate-950">
      <Navbar />

      <main className="flex-1 overflow-hidden px-4 py-4 sm:px-6 lg:px-8">
        <div className="mx-auto flex min-h-[calc(100vh-5rem)] max-w-6xl flex-col gap-5 py-4">
          <div className="flex flex-1 flex-col overflow-hidden rounded-[2rem] border border-slate-200 bg-white shadow-[0_30px_90px_-45px_rgba(15,23,42,0.18)]">
            <div className="border-b border-slate-200 bg-slate-50/80 px-5 py-5 sm:px-7 sm:py-6">
              <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                <div>
                  <p className="text-xs font-semibold uppercase tracking-[0.3em] text-slate-500">
                    AI Agent
                  </p>
                  <h1 className="mt-2 text-2xl font-semibold text-slate-950 sm:text-3xl">
                    Chat with your assistant
                  </h1>
                  <p className="mt-2 max-w-2xl text-sm leading-6 text-slate-500 sm:text-base">
                    Enter to send, Shift+Enter for a newline, and enjoy the responsive conversation view.
                  </p>
                </div>
                <div className="flex flex-col items-start gap-3 sm:items-end sm:flex-row sm:gap-4">
                  <UploadButton onClick={triggerUpload}>Upload PDF</UploadButton>
                  <input
                    ref={fileInputRef}
                    type="file"
                    accept="application/pdf"
                    className="hidden"
                    onChange={onFileChange}
                  />
                </div>
              </div>

              {uploadMessage && (
                <div
                  className={`mt-5 rounded-2xl px-4 py-3 text-sm font-medium shadow-sm ${
                    uploadStatus === "success"
                      ? "bg-emerald-100 text-emerald-900"
                      : "bg-rose-100 text-rose-900"
                  }`}
                >
                  {uploadMessage}
                </div>
              )}
            </div>

            <div className="flex-1 overflow-hidden bg-slate-50">
              <div className="h-full overflow-y-auto px-4 py-6 sm:px-6 sm:py-8 scroll-smooth">
                <div className="mx-auto flex max-w-3xl flex-col gap-4">
                  {messages.map((message, index) => (
                    <Message
                      key={`${message.author}-${index}-${message.content.slice(0, 20)}`}
                      author={message.author}
                      content={message.content}
                    />
                  ))}
                  <div ref={messagesEndRef} />
                </div>
              </div>
            </div>

            <div className="border-t border-slate-200 bg-slate-100 px-4 py-5 sm:px-6">
              <ChatInput value={query} onChange={setQuery} onSend={handleSend} isSending={isSending} />
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
