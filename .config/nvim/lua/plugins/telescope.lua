return {
	"nvim-telescope/telescope.nvim",
	cmd = "Telescope",
	dependencies = {
		"nvim-lua/plenary.nvim",
		"nvim-telescope/telescope-fzf-native.nvim",
	},
	prompt_prefix = " ",
	selection_caret = " ",
	path_display = { "smart" },
	keys = {
		{ "<leader>ff", "<cmd>Telescope find_files<cr>", desc = "Find Files (Root Dir)" },
		{ "<leader>fg", "<cmd>Telescope git_files<cr>", desc = "Find Files (git-files)" },
		{
			"<leader>fb",
			"<cmd>Telescope buffers sort_mru=true sort_lastused=true ignore_current_buffer=true<cr>",
			desc = "Buffers",
		},
		{ "<leader>fs", "<cmd>Telescope grep_string<cr>", desc = "Grep string under cursor in working dir" },
	},
}
