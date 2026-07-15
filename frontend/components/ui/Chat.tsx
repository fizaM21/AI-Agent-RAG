import * as React from "react"

import { cn } from "@/lib/utils"

function Chat({ className, children, ...props }: React.ComponentProps<"section">) {
  return (
    <section className={cn("flex-1 overflow-hidden", className)} {...props}>
      <div className="mx-auto flex h-full max-w-6xl flex-col px-4 py-6 sm:px-6 lg:px-8">
        {children}
      </div>
    </section>
  )
}

export { Chat }
