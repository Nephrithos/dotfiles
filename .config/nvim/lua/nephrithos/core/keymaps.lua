local keymap = vim.keymap
local opts = { noremap = true, silent = true }

vim.g.mapleader = " "
keymap.set("n", "<leader>pv", vim.cmd.Ex)
keymap.set("n", "<leader>nb", ":bnext<CR>")
keymap.set("n", "<leader>pb", ":bprevious<CR>")

-- Select all
keymap.set("n", "<C-a>", "gg<S-v>G")

-- Save file and quit
keymap.set("n", "<Leader>w", ":update<Return>", opts)
keymap.set("n", "<Leader>q", ":bd<Return>", opts)
keymap.set("n", "<Leader>Q", ":qa<Return>", opts)

-- LazyGit
keymap.set("n", "<leader>lg", ":Neogit cwd=", opts)
