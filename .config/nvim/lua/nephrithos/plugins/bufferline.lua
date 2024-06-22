return {
	"akinsho/bufferline.nvim",
	version = "*",
	dependencies = { "nvim-tree/nvim-web-devicons" },
	opts = {
		options = {
			mode = "buffers",
			offsets = {
				{
					filetype = "NvimTree",
					text = function()
						return vim.fn.getcwd()
					end,
					separator = true,
					highlight = "Directory",
				},
			},
			separator_style = "slant",
			indicator = { style = "underline" },
			color_icons = true,
			show_buffer_icons = true,
			show_buffer_close_icons = true,
			show_close_icon = true,
			show_tab_indicators = true,
			always_show_bufferline = true,
		},
	},
}
