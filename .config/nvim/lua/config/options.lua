-- Basic Settings
vim.o.number = true -- Enable line numbers
vim.o.relativenumber = true -- Enable relative line numbers
vim.o.tabstop = 4 -- Number of spaces a tab represents
vim.o.shiftwidth = 4 -- Number of spaces for each indentation
vim.o.expandtab = true -- Convert tabs to spaces
vim.o.smartindent = true -- Automatically indent new lines
vim.o.wrap = false -- Disable line wrapping
vim.opt.undodir = os.getenv("HOME") .. "/.vim/undodir" -- Undo file location
vim.opt.undofile = true -- Create undo file
vim.opt.hlsearch = true -- Hightlight search term
vim.opt.incsearch = true -- Search on each letter
vim.o.cursorline = true -- Highlight the current line
vim.o.termguicolors = true -- Enable 24-bit RGB colors
vim.o.clipboard = "unnamed,unnamedplus"
vim.opt.completeopt = { "menu", "menuone", "noselect" }
vim.opt.smoothscroll = true

-- Syntax highlighting and filetype plugins
vim.cmd("syntax enable")
vim.cmd("filetype plugin indent on")
