return {
	{
		"echasnovski/mini.nvim",
		version = false,
		config = function()
			require("mini.pairs").setup()
			require("mini.surround").setup()
			require("mini.comment").setup()
			require("mini.ai").setup()
			require("mini.icons").setup()
			--require("mini.extra").setup()
			require("mini.hipatterns").setup()
			require("mini.cursorword").setup()
			require("mini.statusline").setup()
			--require("mini.animate").setup()
			require("mini.map").setup()
			--require("mini.notify").setup()
		end,
	},
}
