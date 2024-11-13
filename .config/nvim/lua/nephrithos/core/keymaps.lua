function Map(mode, lhs, rhs, opts)
	local options = { noremap = true, silent = true }
	if opts then
		options = vim.tbl_extend("force", options, opts)
	end
	vim.keymap.set(mode, lhs, rhs, options)
end

vim.g.mapleader = " "
Map("n", "<leader>pv", vim.cmd.Ex)
Map("n", "<leader>nb", ":bnext<CR>")
Map("n", "<leader>pb", ":bprevious<CR>")

-- better movments
Map("n", "<C-h>", "<C-w>h")
Map("n", "<C-j>", "<C-w>j")
Map("n", "<C-k>", "<C-w>k")
Map("n", "<C-l>", "<C-w>l")
-- Select all
Map("n", "<C-a>", "gg<S-v>G")

-- Save file and quit
Map("n", "<Leader>w", ":update<Return>", opts)
Map("n", "<Leader>q", ":bd<Return>", opts)
Map("n", "<Leader>Q", ":qa<Return>", opts)

-- LazyGit
Map("n", "<leader>lg", ":Neogit cwd=", opts)

-- better resize
Map("n", "<C-Down>", ":resize -2<CR>")
Map("n", "<C-Up>", ":resize +2<CR>")
Map("n", "<C-Left>", ":vertical resize -2<CR>")
Map("n", "<C-Right>", ":vertical resize +2<CR>")
-- terminal resize
Map("t", "<C-Up>", "<cmd>resize -2<CR>")
Map("t", "<C-Down>", "<cmd>resize +2<CR>")
Map("t", "<C-Left>", "<cmd>vertical resize -2<CR>")
Map("t", "<C-Right>", "<cmd>vertical resize +2<CR>")

--move blocks
Map("v", "J", ":m '>+1<CR>gv=gv")
Map("v", "K", ":m '<-2<CR>gv=gv")

--indent
Map("v", "<", "<gv")
Map("v", ">", ">gv")

-- Telescope
Map("n", "<leader>ff", "<cmd>Telescope find_files<cr>", { desc = "Fuzzy find files in cwd" })
Map("n", "<leader>fr", "<cmd>Telescope oldfiles<cr>", { desc = "Fuzzy find recent files" })
Map("n", "<leader>fs", "<cmd>Telescope live_grep<cr>", { desc = "Find string in cwd" })
Map("n", "<leader>fc", "<cmd>Telescope grep_string<cr>", { desc = "Find string under cursor in cwd" })

-- space before paste
Map("n", "<leader>p", "li<space><esc>p")
