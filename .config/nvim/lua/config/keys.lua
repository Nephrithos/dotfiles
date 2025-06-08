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
