import * as React from "react"

import { cn } from "@/lib/utils"

function UploadButton({ className, ...props }: React.ComponentProps<"button">) {
  return (
    <button
      type="button"
      className={cn(
        "inline-flex items-center justify-center rounded-full bg-slate-950 px-4 py-2 text-sm font-semibold text-white transition hover:bg-slate-800 disabled:opacity-50 disabled:cursor-not-allowed",
        className
      )}
      {...props}
    />
  )
}

export { UploadButton }
