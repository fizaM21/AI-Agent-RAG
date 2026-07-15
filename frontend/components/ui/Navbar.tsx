import * as React from "react"

import { cn } from "@/lib/utils"

interface NavbarProps extends React.HTMLAttributes<HTMLElement> {
  title?: string
}

function Navbar({ title = "AI Agent", className, ...props }: NavbarProps) {
  return (
    <header
      className={cn(
        "sticky top-0 z-50 border-b border-slate-800/20 bg-slate-950/95 shadow-sm backdrop-blur-xl",
        className
      )}
      {...props}
    >
      <div className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-4 py-4 sm:px-6 lg:px-8">
        <div>
          <p className="text-xs font-semibold uppercase tracking-[0.32em] text-slate-400">
            {title}
          </p>
          <h1 className="mt-1 text-xl font-semibold tracking-tight text-white">
            Modern assistant interface
          </h1>
        </div>

        <div className="hidden items-center gap-2 rounded-full bg-white/10 px-3 py-2 text-sm text-slate-200 ring-1 ring-white/10 sm:flex">
          Light chat • Responsive
        </div>
      </div>
    </header>
  )
}

export { Navbar }
