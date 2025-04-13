return {
	"williamboman/mason.nvim",
	dependencies = {
		"williamboman/mason-lspconfig.nvim",
		"WhoIsSethDaniel/mason-tool-installer.nvim",
	},

	config = function()
		-- import mason
		local mason = require("mason")

		-- import mason-lspconfig
		local mason_lspconfig = require("mason-lspconfig")

		local mason_tool_installer = require("mason-tool-installer")
		-- enable mason and configure icons
		mason.setup({
			ui = {
				icons = {
					package_installed = "✓",
					package_pending = "➜",
					package_uninstalled = "✗",
				},
			},
		})

		require("mason-lspconfig").setup({
			ensure_installed = {
				"lua_ls",
				"rust_analyzer",
				"bashls",
				"css_variables",
				"cssls",
				"cssmodules_ls",
				"tailwindcss",
				"unocss",
				"jinja_lsp",
				"docker_compose_language_service",
				"dockerls",
				"ast_grep",
				"html",
				"lwc_ls",
				"stimulus_ls",
				"superhtml",
				"templ",
				"twiggy_language_server",
				"biome",
				"denols",
				"eslint",
				"glint",
				"grammarly",
				"markdown_oxide",
				"basedpyright",
				"pylsp",
				"ruff",
				"sqlls",
				"ts_ls",
				"yamlls",
				"diagnosticls",
				"vuels",
			},

			automatic_installation = true, -- not the same as ensure_installed
		})
		mason_tool_installer.setup({
			ensure_installed = {
				"prettier", -- prettier formatter
				"stylua", -- lua formatter
				"isort", -- python formatter
				"black", -- python formatter
				"clang-format",
			},
		})
	end,
}
