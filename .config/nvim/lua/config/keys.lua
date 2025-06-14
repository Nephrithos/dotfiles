local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }
-- Leader key
vim.g.mapleader = " " -- Space as the leader key

local n = "n"
vim.keymap.set(n, "<leader>dk", function()
	require("dap").continue()
end)
vim.keymap.set(n, "<leader>dl", function()
	require("dap").run_last()
end)
vim.keymap.set(n, "<leader>b", function()
	require("dap").toggle_breakpoint()
end)
vim.keymap.set(n, "<leader>l", "<cmd>Lazy<cr>", { desc = "Open Lazy plugin manager" })
vim.keymap.set(n, "-", "<cmd>Oil --float<cr>", { desc = "Open file browser Oil" })

vim.keymap.set(n, "<leader>u", vim.cmd.UndotreeToggle)

-- Barbar

-- Move to previous/next
map(n, "<A-,>", "<Cmd>BufferPrevious<CR>", opts)
map(n, "<A-.>", "<Cmd>BufferNext<CR>", opts)

-- Re-order to previous/next
map(n, "<A-<>", "<Cmd>BufferMovePrevious<CR>", opts)
map(n, "<A->>", "<Cmd>BufferMoveNext<CR>", opts)

-- Goto buffer in position...
map(n, "<A-1>", "<Cmd>BufferGoto 1<CR>", opts)
map(n, "<A-2>", "<Cmd>BufferGoto 2<CR>", opts)
map(n, "<A-3>", "<Cmd>BufferGoto 3<CR>", opts)
map(n, "<A-4>", "<Cmd>BufferGoto 4<CR>", opts)
map(n, "<A-5>", "<Cmd>BufferGoto 5<CR>", opts)
map(n, "<A-6>", "<Cmd>BufferGoto 6<CR>", opts)
map(n, "<A-7>", "<Cmd>BufferGoto 7<CR>", opts)
map(n, "<A-8>", "<Cmd>BufferGoto 8<CR>", opts)
map(n, "<A-9>", "<Cmd>BufferGoto 9<CR>", opts)
map(n, "<A-0>", "<Cmd>BufferLast<CR>", opts)

-- Pin/unpin buffer
map(n, "<A-p>", "<Cmd>BufferPin<CR>", opts)

-- Goto pinned/unpinned buffer
--                 :BufferGotoPinned
--                 :BufferGotoUnpinned

-- Close buffer
map(n, "<A-c>", "<Cmd>BufferClose<CR>", opts)
map(n, "<A-q>", "<Cmd>BufferCloseAllButCurrentOrPinned<CR>", opts)
-- Close commands
--                 :BufferCloseAllButCurrent
--                 :BufferCloseAllButPinned
--                 :BufferCloseAllButCurrentOrPinned
--                 :BufferCloseBuffersLeft
--                 :BufferCloseBuffersRight

-- Magic buffer-picking mode
map(n, "<C-p>", "<Cmd>BufferPick<CR>", opts)
map(n, "<C-s-p>", "<Cmd>BufferPickDelete<CR>", opts)

-- Sort automatically by...
map(n, "<leader>bb", "<Cmd>BufferOrderByBufferNumber<CR>", opts)
map(n, "<leader>bn", "<Cmd>BufferOrderByName<CR>", opts)
map(n, "<leader>bd", "<Cmd>BufferOrderByDirectory<CR>", opts)
map(n, "<leader>bl", "<Cmd>BufferOrderByLanguage<CR>", opts)
map(n, "<leader>bw", "<Cmd>BufferOrderByWindowNumber<CR>", opts)
