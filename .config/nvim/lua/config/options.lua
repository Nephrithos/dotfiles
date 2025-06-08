-- Basic Settings
vim.o.number = true -- Enable line numbers
vim.o.relativenumber = true -- Enable relative line numbers
vim.o.expandtab = true --Convert tabs to spaces
vim.o.tabstop = 4 -- Number of spaces a tab represents
vim.o.shiftwidth = 4 -- Number of spaces for each indentation
vim.opt.softtabstop = 4 -- How many spaces are applied when pressing Tab
vim.o.expandtab = true -- Convert tabs to spaces
vim.o.smartindent = true -- Automatically indent new lines
vim.o.smarttab = true
vim.o.autoindent = true
vim.o.breakindent = true
vim.o.undofile = true
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.list = true
vim.opt.listchars = { tab = "» ", trail = "·", nbsp = "␣" }
vim.o.mouse = "a"
vim.o.showmode = false
vim.o.signcolumn = "yes"
vim.o.splitright = true
vim.o.splitbelow = true
vim.o.scrolloff = 10


-- Minimal number of screen lines to keep above and below the cursor.
vim.opt.scrolloff = 5
vim.o.wrap = false -- Disable line wrapping
vim.o.cursorline = true -- Highlight the current line
vim.o.termguicolors = true -- Enable 24-bit RGB colors
vim.o.clipboard = "unnamed,unnamedplus"
vim.opt.completeopt = { "menu", "menuone", "noselect" }

-- Syntax highlighting and filetype plugins
vim.cmd("syntax enable")
vim.cmd("filetype plugin indent on")
