return {
	{
		"folke/snacks.nvim",
		priority = 1000,
		lazy = false,
		---@type snacks.Config
		opts = {
			explorer = {
				enabled = true,
				replace_netrw = true,
				hidden = true,
				ignored = true,
				exclude = { "node_modules", ".git" },
			},
			picker = {
				sources = {
					projects = {
						dev = {},
					},
					files = {
						hidden = true,
						ignored = true,
					},
				},
				-- show hidden files like .env
				hidden = true,
				-- show files ignored by git like node_modules
				ignored = true,
			},
			notifier = {
				enabled = true,
				timeout = 3000,
			},
			terminial = {
				win = { style = "terminial" },

				bo = {
					filetype = "snacks_terminal",
				},
				wo = {},
				keys = {
					q = "hide",
					gf = function(self)
						local f = vim.fn.findfile(vim.fn.expand("<cfile>"), "**")
						if f == "" then
							Snacks.notify.warn("No file under cursor")
						else
							self:hide()
							vim.schedule(function()
								vim.cmd("e " .. f)
							end)
						end
					end,
					term_normal = {
						"<esc>",
						function(self)
							self.esc_timer = self.esc_timer or (vim.uv or vim.loop).new_timer()
							if self.esc_timer:is_active() then
								self.esc_timer:stop()
								vim.cmd("stopinsert")
							else
								self.esc_timer:start(200, 0, function() end)
								return "<esc>"
							end
						end,
						mode = "t",
						expr = true,
						desc = "Double escape to normal mode",
					},
				},
			},
		},

		keys = {
			{
				"<leader>e",
				function()
					Snacks.explorer()
				end,
				desc = "File Explorer",
			},
			{
				"<leader>fe",
				function()
					Snacks.explorer({ cwd = "/home/nephrithos/" })
				end,
				desc = "Explorer Snacks (root dir)",
			},
			{ "<leader>E", "<leader>fe", desc = "Explorer Snacks (root dir)", remap = true },
			{
				"<c-/>",
				function()
					Snacks.terminal()
				end,
				desc = "Toggle Terminal",
			},
		},
	},
}
